def usd_to_inr(usd_amount, exchange_rate=83.0):

    return usd_amount * exchange_rate


usd = 10
inr = usd_to_inr(usd)
print(f"{usd} USD is equal to {inr} INR")   