#Program:
s=input()
at=s.index('@')
dot=s.index('.')
username=s[:at]
domain=s[at+1:dot]
exten=s[dot+1:]
print(exten)
print(domain)
print(username)
