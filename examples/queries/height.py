from mantrapy.querier.querier import API, RPC, Querier

querier = Querier(API, RPC)


height_resp = querier.get_height()
print(height_resp.data)
