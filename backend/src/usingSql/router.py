from fastapi import APIRouter, Query, HTTPException, Depends, Request
from utils.parser import Parser
import json 
from .service import db
from dependencies.redis import get_redis

router = APIRouter(
    prefix="/sql",
    tags=["SQL"]
    )   

@router.get('/lookup_whois')
async def lookup_whois(request: Request, domain_name: str = Query(..., description="Domain name to look up in WHOIS"), redis=Depends(get_redis)):
    log = await db.add_logs(domain_name, request.client.host)

    response = {"log": log}
    try:
        cached_data = await redis.get(domain_name)
        if cached_data:
            response.update({"detail": json.loads(cached_data)})
            return response

        parser = Parser(domain_name)
        info = await parser.run()

        if "error" in info:
            raise HTTPException(status_code=400, detail=info["error"])

        await redis.set(domain_name, json.dumps(info), ex=86400)
        response.update({"info": info})

    except HTTPException as he:
        response.update({"error": str(he.detail)})
        raise

    return response
