from extension import db
from datetime import datetime
from zoneinfo import ZoneInfo

class Tarea(db.Model):
    __tablename__ = 'tareas'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    completada = db.Column(db.Boolean, default=False)

    # Fecha con zona horaria Bolivia
    fecha_creacion = db.Column(
        db.DateTime,
        default=lambda: datetime.now(ZoneInfo("America/La_Paz"))
    )

    def __repr__(self):
        return f'<Tarea {self.titulo!r}>'