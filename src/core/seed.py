import os
import json
from datetime import datetime
from src.core.models.database import db
from src.core.models import Filial

def cargar_datos(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(dir_path, 'data', filename)
    with open(full_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def eliminar_y_agregar(entidad, datos):
    db.session.query(entidad).delete()
    for data in datos:
        if 'fecha_nacimiento' in data:
            data['fecha_nacimiento'] = datetime.fromisoformat(data['fecha_nacimiento'])
        db.session.add(entidad(**data))

def seed_db():
    try:
        entidades_datos = {
            Filial: 'filiales.json',
        }
        
        for entidad, archivo in entidades_datos.items():
            datos = cargar_datos(archivo)
            eliminar_y_agregar(entidad, datos)

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {e}")

