
import os

from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


DATABASE_URL = "sqlite:///./produtos.db"
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/produtos", status_code=200)
def listar_produtos(db: Session = Depends(obter_db)):
    produtos = db.query(Produto).all()
    return produtos

@app.post("/produtos", status_code=201)
def criar_produto(nome: str, descricao: str, db: Session = Depends(obter_db)):
    if not nome or not descricao:
        raise HTTPException(status_code=400, detail="Nome e descrição são obrigatórios.")

    novo_produto = Produto(nome=nome, descricao=descricao)
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

@app.put("/produtos/{produto_id}", status_code=200)
def atualizar_produto(produto_id: int, nome: str, descricao: str, db: Session = Depends(obter_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        raise HTTPException(status_code=400, detail="Produto não encontrado.")

    produto.nome = nome
    produto.descricao = descricao
    db.commit()
    db.refresh(produto)
    return produto

@app.delete("/produtos/{produto_id}", status_code=200)
def deletar_produto(produto_id: int, db: Session = Depends(obter_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        raise HTTPException(status_code=400, detail="Produto não encontrado.")

    db.delete(produto)
    db.commit()
    return {"mensagem": "Produto deletado com sucesso."}

@app.get("/simular-erro-500", status_code=500)
def simular_erro_interno():
    raise HTTPException(status_code=500, detail="Erro interno do servidor simulado.")
