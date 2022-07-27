import dropbox

class TransferData:
    def __init__(self, accToken):
        self.accToken = accToken

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.accToken)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    accToken = 'sl.BLVAMG2uQ1dkK1YXPElzyDQJQiH4ONmdX1147gYjdyWXGD7SQYQNbFZPRkZG49fpJp1EpJEV1g-NnB_ByIZoBU07semmydJc2Mu1MmCjgu85CSpFgx26LPMB7ReWluXm3ytuSg4'
    
    transfer = TransferData(accToken)

    file_from = input("Enter local file path: ")
    file_to = input("Enter dropbox file path: ")

    transfer.upload_file(file_from, file_to)
    print('File uploaded')

main()