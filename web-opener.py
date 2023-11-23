import webbrowser

def open_websites():
    # List of websites you want to open
    websites = [
        "https://mempool.space/block/000000000000000000005cb4f1026adc77c773081ee06cedf316c898a75dae5c",
        "https://timechaincalendar.com/en",
        "https://bitcoinwhitepaper.co/?msclkid=e85cea2bd12611ec81d5eb44f9d1c110",
        "https://www.lopp.net/bitcoin-information/technical-resources.html#core",
        "https://www.lynalden.com/"
    ]

    for website in websites:
        webbrowser.open(website)

if __name__ == "__main__":
    open_websites()