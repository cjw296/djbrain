import discogs_client

token = open('.token').read()


def main():
    d = discogs_client.Client('djbrain/0.0.0', user_token=token)
    # 5018515906514
    barcode = input('barcode:')
    print(barcode)
    results = d.search(barcode=barcode)
    print(results.count)
    # print(results)
    r = d.release(results[0].id)
    r.title
    pass


if __name__ == '__main__':
    main()
