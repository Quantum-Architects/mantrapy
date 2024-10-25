from mantrapy.querier.querier import API, RPC, Querier

querier = Querier(API, RPC)


tx_resp = querier.get_tx_by_hash(
    "0xC414DBB9C80503DFF20684536710FD4FC0401B39C25B0171C752ABCE3907CD95"
)
print(tx_resp)
