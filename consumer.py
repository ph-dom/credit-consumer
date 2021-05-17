from suds.client import Client

client = Client("http://localhost:58939/WebService.asmx?WSDL")

def ValidateTransaction (PAN, ExpirationMonth, ExpirationYear, SecurityCode, CardBrand, Password, TransactionAmount) :
    transaction = client.factory.create("Transaction")

    transaction.PAN = PAN
    transaction.ExpirationMonth = ExpirationMonth
    transaction.ExpirationYear = ExpirationYear
    transaction.SecurityCode = SecurityCode
    transaction.CardBrand = CardBrand
    transaction.Password = Password
    transaction.TransactionAmount = TransactionAmount

    result = client.service.ValidateTransaction(transaction)
    
    return result
