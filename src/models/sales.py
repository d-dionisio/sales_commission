from database import db

# nome, telefone, valor, plano, seguro e data
class Sales(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(80), nullable=False)
    telephone = db.Column(db.String(80), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    flat = db.Column(db.String(80), nullable=False)
    insurance = db.Column(db.String(10))
    create_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, customer, telephone, value, flat, insurance) -> None:
        self.customer = customer
        self.telephone = telephone
        self.value = value
        self.flat = flat
        self.insurance = insurance

    # def to_dict(self):
    #     return {
    #         "customer": self.customer,
    #         "telephone": self.telephone,
    #         "value": self.value,
    #         "flat": self.flat,
    #         "insurance": self.insurance,
    #         "date": self.date
    #     }