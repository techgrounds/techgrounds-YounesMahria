# Asymmetric encryption
Uitleg en werking van Asysmmetric Encryption gebruiken.

## Key-terms

### Asymmetrical encryption  
Deze versleutelingsmethode verschilt van asymmetrische versleuteling waarbij  een openbare Sleutel en een privésleutel wordt gebruikt om berichten te versleutelen en ontsleutelen.

### RAS  
Rivest-Shamir-Adleman (RSA) is een een asymmetrische coderingstechniek die twee verschillende sleutels gebruikt als openbare en privésleutels om de codering en decodering uit te voeren. Hiermee kunt u als volgt:
* Openbare Sleutel: Het Versleutelen van Gevoelige Informatie.
* Privésleutel: Het Ontsleuten van het Versleutelde bericht.
Het wordt meestal gebruikt bij 2 verschillende eindpunten:
* VPN
* SSH


## Opdracht

### Generate a key pair.

**Private key**
```
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
```
*Disclaimer: Dit staat alleen genoteerd voor opdracht zelf. In het pratijk zou ik dit niet posten, heeft wel typefouten. -Reactie aan GitGuardian (good bot)

**Public Key**
```
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEApCGvwJ8NuVD7c9NhM5drj5qh6AKsUZVwTnLun9yEyXHVTERiosViozTyDpYR9LRbvzMzINrvjyLVZHH/g57qJCyhOwxE29zW44FXm+ICoEivydPrFmIevk0QNUTZTXuyhxRUV44Z+hpJYjnO+MEZiV99cIf+KiIn87704Ks+0Z60rxJtHRTBiZ62Pf+SirAsFJG0faWJ8hEkCEMtIkD2d9i4LGkT7OoGUNZ+Ppx9IoR1Ieah5N5VqqESGIhPTVyaMnuqBxlUm1OO1EAhe4d+5cV+NlQl9ugABZqojaeC2HWbPQedIP8n8uQAlzRer4LjHFbfMT4Wqn+jn/2bQ+9V7NMrRLnRKEXAxgyT6lMY6VzQ40grOjyDd+jS4g84oUjD8R/UYEM7dsDKWO/l2cKFNB85X5PF1tXWbjbc7AO823nRezNkyaAMELXLasKiTp8aRSQxa2woS3fd9d+du+rQhO/CfoUKq6FA5jHbRMhk4J6B3ZtSziZAlHnK7PtV/cFHsU0NydBR+HGO48TcnSb5rDJbsFV8Ke7Owz4xA995+y15UOuN0NvfWdHFoRY1x6AIILkRZDjX1rxQ9BAya19d9FbDuKRue2fx6D2uY6XbGsXSxREw3AQyU9yc5UXhcxpAuBgVKHD5lHHvu8AYWBiEbIbwy/o1vrgSjK5GfoXg048CAwEAAQ==
-----END PUBLIC KEY-----
```

**Text to encrypt**
```
Kan je dit lezen zeg: Ja, geeft mij nu de antwoord voor opgave 4
```

**Encrypted**
```
bqBM7+O/aNJrRbJjr6YaQ/Tg6PJPE6koOgISuBWpHziHwJV1zBCxZq/bxOPN5I+P0Z9brC25D6bCH4I//T6c6eZ6SmJ+d3Hig8YWx+1zhtPu9kAwihsi9BizpQZQNUpDJM7uub67Wg/bhhMnocDybJRMjjs8dBsbHx4ag1dQierumoOA+SNInnA62kqRM1Rf/KPhYv6cpEff3lSfJc9Ls2SMYTp4oSa3NlcrSrmkq2E+XNkdnt/xLaIHo2F3ra/mhoPBfjL//UKab411Ld6EZqTLqgu8JVfADLZlS2dstAwp9L1SpGHTNXrLdbVaHYPsBzYTm+/Pt8aUitWbRXifhm5iYj1Qg9wTMVO2rcJ6UbrGfoeN10DecqMdqmpqJigE7C7B9rlLy8DANou6bmyo/TbdDA4ZUdV89Ky7yWUchb3bv+Stl2iH72hvymGz1zBsdHhMPQZ1iYnVlMe1bRyrx7vwz+RhE4yUkYdnubQzUzmN9qh39I0zjwmHrHmJ/N7MMaHNMAHKmduLVzg9uTKpVlYsj3oExt0EkXxl49D/JIzm0LgKqMGLH1dKEynIXcVv0w3RRgn977RlfyuqFdJN8WVGpM/Yg9IbxPH1BgXRX+tPh3HmepTqUtcACC3VLH7RRR21zfdx7b/i8sFhjEDWb1B4LqKPa0D2Yb/QCN5nr+Q=
```

### Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key. The recipient should be able to read the message, but it should remain a secret to everyone else. You are not allowed to use any private messages or other communication channels besides the public Slack channel. Analyse the difference between this method and symmetric encryption.

### Team 3 - Week 2

### Quincy  

**Text to encrypt**
```
Als je de antwooord nodig hebt van mij vorige sleutel, kijk goed naar de hoofdletters.
```

**Public Key**
```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCjgzMrgBJBmp+H6IjrGOKVWE8FcMyI7QQj1Uqqu9joqjoa7HGu5iv4ZC4rS+JBQyXy9LmTGaRyNOuRrMEsYDqWOy86cqE/Zl+gJekxC/APD7vS+2BoU45jNhu6+/QvDP+LF+0rlJi4t+Qy7ey25gVbhL+U+n+LL1JL0n5+55UAuwIDAQAB
-----END PUBLIC KEY-----
```

**Encrypted Output**  
```
RiKw4nqPilFs9Ka0ZJBYmjAVqi/KlcdBb2euC2RP66H2df23sXvECGRhP8elcKOUDYj9IqlVifgDPtsoiKLG9z9WaDA3G2dx1Ttlco7QcP9uVy4jyrZQlxqOwidbTAw9i4pLqGVkobKvfz6mB5j2Lrq/m7Jij86aOPwiKVpIu9c=
```

**Naar mij**:  
**Encrypted Input**  
```
gAU9ofYOkpm5i5IvryX5TURPcTii7hL9hxQJExf80iV/jHrN/g6KRBdenRC0tEzcWnFKvRkajtZZM7XAY45gAJts2GTYFc+8+f/ALHq2F5xFOAmDN5cHLs5z5BnbBwsnmxWIXs7WcOK3UPCeSsy760lm6iOoLaaL65KP3u8NNajraUQY5K/1TroJWjzQe++qaleiLF7dbH/WQyZOAR2JoSw50acpQ1LnfUtQ6WLVYFsQA1lkp2Djjkcux8kjhQB+52L28Xcez2jLJ2oOuUmfG81Wo7gzjCYMVhTc3UiJ6UCXXTmZv1K3hC62KKE61/VUwFijRYjnSd+S7E4/Ung3sl4wK7My6mkjxItZ7pHlMb6Bc/7WkSBHKeOzxL8zU7oa5h0/qzIUMxmYuvMzeYMNt4ekZoqGdjyRo21W9eCfEy4PxENX82VwaAjV+j5eIxaEiEkdMCwAe90H7WS4uYH+Wm21MC2iH/7hsIqWViRbi9OYBAwPO0B/e9UjNIB4Yledgd11n07r3k6L/1sZ4xGtN68F1797N5a4BOSn2C5LsLLaOOwgCKPm+HpCRfuqGXuFQjF8KMpJOEQvPPztyqQ1PBQ+PaxrDmk8S+EThwKM2YIkzIC61mUgkTHmm3lWMUchJ15k+lrqxYNVWTaANOI2U/crpZkojJkS1QlpwjLIucI=
```

**Decrypted Output**
```
Nee, sorry ik weet het niet. Het is te moeilijk voor mij hahaha. Maar wel mooi gedaan!
```

### Roan  

**Text to encrypt**
```

```

**Public Key**
```
-----BEGIN PUBLIC KEY-----

-----END PUBLIC KEY-----
```

**Encrypted Output**  
```
BF4ySQ29SkFuWEUOSwi9EzZ+sW8ETceaPEV83Mmisj5Y0EOAIhzA/1cg5/DL1TGmIZhzy9pWgok+GD6Onsf0F9/bj1wiA/ZHe6Bqe41oSTOq+g/kRCOTrs3lNTont9v/NsaGtjm0aS5iCffSBYZxfAMtP73kHa27nMFKIs6KlPI=
```

**Naar mij**:  
**Encrypted Input**  
```

```

**Decrypted Output**
```

```

### Jon  

**Text to encrypt**
```
Goed gedaan! Go zo door!
```

**Public Key**
```
-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgFGBp2kNZlPJOxYeBbmQ0P6YQD/E
Gjmg/Tq+H/AKAzK9GsvdP3dXDfRMax71or5hLYPIpRNUkDWOOITWShn9doJ75JBw
cSlNgi30lDNSyfA01C0ByG3i6dmhOy4ktGqUPmyJ7y9oezEZEvcEMAKW7tVnpvkl
p4ZaHhPrkGZ+6KXhAgMBAAE=
-----END PUBLIC KEY-----
```

**Encrypted Output**  
```
BF4ySQ29SkFuWEUOSwi9EzZ+sW8ETceaPEV83Mmisj5Y0EOAIhzA/1cg5/DL1TGmIZhzy9pWgok+GD6Onsf0F9/bj1wiA/ZHe6Bqe41oSTOq+g/kRCOTrs3lNTont9v/NsaGtjm0aS5iCffSBYZxfAMtP73kHa27nMFKIs6KlPI=
```

**Naar mij**:  
**Encrypted Input**  
```
nJ8z8miwW9UfmIxxVN780q1H48tPoK83swDZFYFTBY+A8pM1TasO2qUmF2rSkOGCK11UzUKpEkfuDuFoJHMSB+PKf5n2y3r84Rdopo6f/N2cQF9bIVDpF5WoDkR+rSTQ11+sTFMdx7NEyqPOvGlXTgrRojaPeL+3P4YD7EoMvjgl9/hW/+af5yq9/NOVmdWN8z6ymlcyzXlCOxuO/H5ugT9C11uGYRPhApGQeHOsVU9YPB8tg5bUwG1HimAwyW/QTlXyPnOOWafu73v6sT9b6nLzJ7268RMe1mK1G/G9+nvbgnV1xXt0WmX8zOzuhBG9acvmwS8ziQW2N/6eg7eyBVDgK7difso33xwAqz8zri79rMqzpkjLfOM9m9uyoY1VLzZlu3DNf2FjPlOhMMAgNZBF3bB/+9xYMzjdZT5e5Daq2nauFokxz0jU9FGN1sL3cUlag9dC2GiAU/WpwgCR5u+vI11msU/6JnGeSwltGow2+F82RQkdAk/UChKOp1TbYesfoOSDS+oZKthV9KJ0sn8Uz5RTTu0KA5u2GE4k8pATsbyRh++tjjDls3IkOKRmltt7X7HfERNYwKoMqARJ02GvDWLVoAEjkqoROz7oIP8wygIv0sdxmMFgYJ5MJ2mnA70Y8d45vBBLBJmNW9SJzrWexlDTgLp2kwFfZF2t3Yk=
```

**Decrypted Output**
```
Ontpit een avocado met een scherp mes door zo hard mogelijk te steken. Zo hoef je helemaal niet naar de eerste hulp.
```

### Gebruikte bronnen
https://www.techopedia.com/definition/1779/hybrid-encryption

### Ervaren problemen
Geen, nadat ik bij vorige opdracht veel beter erover had geleerd was deze opdracht makkelijker te doen.

### Resultaat
Het versturen van geheime berichten zonder dat andere weten wat er gestuurd is en dat ik alleen berichten die voor mij bedoeld is gelezen kunnen worden. 

*Disclaimer: De privésleutel staat alleen genoteerd voor opdracht zelf. In het pratijk zou ik dit niet posten. 