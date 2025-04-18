import json
import csv

with open("../docs/transaction-presentation-service-response.json", encoding="utf-8") as json_file:
    response_obj = json.load(json_file)

with open("transactions-output.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL, quotechar="\"")
    field = ["date", "description", "credit", "debit"]
    writer.writerow(field)

    for transaction in response_obj["transactionList"]:
        writer.writerow([
            transaction["postedDate"],
            transaction["description"][0],
            float(transaction["amount"]) if transaction["creditDebitIndicator"] == "CREDIT" else None,
            float(transaction["amount"]) if transaction["creditDebitIndicator"] == "DEBIT" else None
        ])
