FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt main.py ./
RUN pip install --no-cache-dir -r requirements.txt
ENV GOPLUTO_MCP_URL=https://api.gopluto.ai/mcp \
    GOPLUTO_AUTH_HEADER=gopluto-api-key \
    GOPLUTO_TRANSPORT=sse
EXPOSE 12006
CMD ["python","main.py","--mode","http","--host","0.0.0.0","--port","12006"]
