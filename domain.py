import whois

domain = "google.com"
info = whois.whois(domain)

print("Домен:", info.domain_name)
print("Регистратор:", info.registrar)
