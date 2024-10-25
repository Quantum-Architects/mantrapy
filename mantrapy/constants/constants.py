import os


class Constants:

    def __init__(self):
        self.rest_endpoint = os.getenv(
            'REST_ENDPOINT',
            'https://api.mantrachain.io',
        )
        self.memo = os.getenv('MEMO', '')
        self.fee = os.getenv('FEE', '20')
        self.gas_limit = os.getenv('GAS_LIMIT', '200000')
        self.chain_id = os.getenv('CHAIN_ID', 'mantra-1')
        self.denom = os.getenv('DENOM', 'uom')

    def testnet(self):
        self.rest_endpoint = 'https://api.dukong.mantrachain.io/'
        self.denom = 'uom'
