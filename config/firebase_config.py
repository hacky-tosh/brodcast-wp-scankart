from google.cloud import firestore
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

load_dotenv()

# service_account_info = {
#     "type": os.getenv("TYPE"),
#     "project_id": os.getenv("PROJECT_ID"),
#     "private_key_id": os.getenv("PRIVATE_KEY_ID"),
#     "private_key": os.getenv("PRIVATE_KEY"),
#     "client_email": os.getenv("CLIENT_EMAIL"),
#     "client_id": os.getenv("CLIENT_ID"),
#     "auth_uri": os.getenv("AUTH_URI"),
#     "token_uri": os.getenv("TOKEN_URI"),
#     "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
#     "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
#     "universe_domain": os.getenv("UNIVERSE_DOMAIN"),
# }

service = {
  "type": "service_account",
  "project_id": "scankart-40ac1",
  "private_key_id": "2f46d4b9fd0abc7f39bb8ab220936d20395409d8",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDSvanefH3DVa3d\nL9alFDHW+Tb1baQ/f4Ir+spse804s2ym4mdgylolPSB2qPlAB2wP6bMelF6/tE5a\nV2GUP776SDlIg0Jys9gPCmi1wn1LQ5nEciClbYPhUuOCLyIAUbDxznHPLeKbfA92\nwnnZNkLI+tJzKdNAbNh0d/CPZKUzS0rN4Dn2AiVcg+/vVp5dXZSgbSPOz9H8RnSz\nVyjRV/IhMFtMyCWJ8RvSf23cfMGoGSEgng5cE7QY+VzH7Nxn9mBfH/0GRkcEleNy\nfDd8DdF9pxiLkpGOkUSLrE+gkiU71hgTOPq1lszagJmUdGbCSk+z4u6mQs7OmwKM\nXHjsU+dzAgMBAAECggEAVv/sskhjpPHomoEm1DSflLeCrFSMs5ggtaZNzfZYFRnh\nd43NDsTK7UescMA2UewefP1GMJAhA3Rcymf7hTfB0FJjr59cnbzILAFok+zMS/eG\n8fYJqzGoeat9998cYtRWv6SyEE1JmVXgjm8f3X/Ml2sQ2XFBYH3u6DohqhjrKF6j\nXDktJp97glyGFIjfy+MNRWqUTo5+qWDw9Lwr01jmoRFQ9FZy7fFfBYGyIfMTXb/9\nRECUoPJJWRG9YKnL2S8zGsI1H9lA3hIhQhNBtaVPVddeTc84VHBzG5e/5yHUYcQV\neBUkhDJ20DGXPV1FzKS7WpPep27NZNanc1QhgPYeUQKBgQD1YiverNOFszpDwODq\nnhl27RXhNZXoZHelPCmPLwZiFaXPOphkG+UlbN304KDMShvoLXI47mgeEisaVIQk\nRpTsUuZzcT1Gla/47SlfB8jbDQbptwMnpu+xIOb5PpdZZsXcKxnku8Zk7qrRsn51\ntaIi8wxCaIjcbts7U1s4JmulYwKBgQDb28vPNjuvTHvehNk66Oe6LKoZHtT9BkRC\nawhLpddQPi65AALKG4oppP70xjK0EQuXJGJ7mHovzNcou+L2wBPRwCp+cKoNii6R\nM7akw5bjzF4eHmH8M1RZ3SY0fHKPzxkRvz/GtsL3DBK4vTXGkNKCCoWjReIO1tZ6\nyKgc4MOasQKBgQDM1XVPfS9Y9ULW2gQmdXFGUCSqiWOoyW0CtpTunE+UwwNVWFFr\nh8mhkx440uYHgnmHN6CYm5K4P2xRn2lrKqwYFh+fEFEZQczSW47kcAgfquExaX8t\ns3F0h8WnG7OVgm/6GNSVlpXHHV/kij58HfHJgN+j88UDVVqWTD/iQFgthwKBgDnV\n4A9qXNkIba1jlSGCEzNOfJCPI8hL1bkDHvOHdNSPBwtzjUhNZlL+LHOHj97+fOYN\nlDqfKcVZRWBZzKLMdGpA+uy4BoP5Tba0u98r9I2IPVn+9Be8CPx6yIoWEqzx9c5N\nWSGVAkSq0GH4pCTQBBBhZDZHM+hja5hxIIg4ODyBAoGAMtrb/lwMXvdHoHM/S9KA\nuKTd3/rLmuuxovQpNJ7C+5pmqR7koUJH63qB6BB4LACsipktHS5Cz8pThXcdPN7B\n9c2G4n4WYWJ0jvAuddJKfiymS9UHjKX7o9gTDirCuGQLs2NvNr0QIyR/p796bL29\nrLuA6noUShbwmmTDj1ARwaY=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-o2pvr@scankart-40ac1.iam.gserviceaccount.com",
  "client_id": "115609852691823809025",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-o2pvr%40scankart-40ac1.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


db = firestore.Client.from_service_account_info(service

)

