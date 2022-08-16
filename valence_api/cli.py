import typer
import uvicorn

app = typer.Typer()


@app.command()
def debug():
    uvicorn.run(
        "valence_api:app.create_app",
        host="localhost",
        port=8000,
        debug=True,
        factory=True,
    )


@app.command()
def deploy():
    uvicorn.run("valence_api:app.create_app", host="*", port=80, factory=True)
