from mantrapy.querier.querier import API
from mantrapy.querier.querier import Querier
from mantrapy.querier.querier import RPC

querier = Querier(API, RPC)

balances_resp = querier.get_balances(
    'mantra1n4u9s9h3c670s7wsfycf6v7d7f2t55ql9gm3sj', )
print(balances_resp)
