from google.cloud import firestore
from google.oauth2 import service_account

service_account_info = {
  "type": "service_account",
  "project_id": "scankart-40ac1",
  "private_key_id": "2d17bcdbfeaecdf2a744d3ae6b29f4bff142cc02",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC0BUc38E8v194A\nLt9GI+cT+2Z+5hIPtfqv680NNnjj1kXNIDAHXTo214aCusurX6zI+kIWUZiaCbxP\n2oKvDkJx4gTYgpE9P5O1RebjiH4VFXqfmmrzOej4/en7OCv6PIARPipZ+SujUETv\no4CQPkrzOmAcjgGxvF4HE38EwW4qC48Roh6gVCwQrBGzXA0Z/vvSvmLaZMvqDQkG\nPzQ4+9Ktt31k326y4oVqJOhn9qEasPijUA+klF9vMI0sLPJNxt79UsrZ4OEOyyZy\nt1f/WCQevHsXpaEH9908OA9qbXKbcEqE6uqZ1WciAhhecUcRjW2PS8Nxt1/0MRUX\nzjSjVkH5AgMBAAECggEAGflo/Tk/M7gB4CTjMkub29Y6Q7UOhhXLxfZP78gcSUNx\nbtdmFqns7FzMm7A4EtILLDRvtKixTAh7k0oD8R4tmCD0cgjky+GQfmdHmSzohEJF\nHyI4rD9+ze5VBFpmfgScteAyXCkHktjSGYGN20IhrlaN55DVzb9QEdVOTnFaY9Zp\nKpJUyuhCYiDhJgVVaghKPn38bHQMgTpX7GV5vg+hIctNLGEwi98qlTqX0CFL8OOu\npLQNtuw9cxxBTHF7nFGcY2ZfXu+gZN6H4dC8bpwnQaJiPPLQsHloRBsgn+8Nk8Pl\nZickaxV01Fn8dc78WejmAdPyz3UvbVp76xitG3zNwQKBgQDYbHplXKXg56riDBFH\nZFO/e2eC12wywJ+VWybGkjawJAiBy8LcOMYaxvJEngzWR8cFpO0ReAs1VGMPQY+I\nqxxBsp6yf05EzSlQuaicK4ls/DrUC8Xg2cAbhTmb4+W/sDY2Eq0cTbuBizwGEuoe\nRhHw9AnbGtGw9RjWIKe7S3tHOwKBgQDU8KXKqmuo4CUM0ERl/15zK13xfRxO8qnY\n2KXoJCJJe+s4d15/EG0+VfRYILuM0n2ruk6RlfVWThYk4eBVxPYuswV0eVrAFlhI\n72cliYEFKgrcV/lfEA5elmouWlsmf1RBOShLa+NSDDF5ZMZXxNfAwYoe026X+FQ0\nax0ny6zQWwKBgDMS1oeZJ6Q9x7v0sRcx+/mSO8lK4UPQ5Vgv3KS72KAUwNUwqtmh\npE6paH789XaUFcmlNDUNKUf6lC4DgMX164Mtjfn9xRDDgd6FEd9Y/uNzWsazyIzZ\nllZoSEIbtBpakVCNc8DcL0XQ/+dHC2z9iDpevPyyBY5HKQdPSYYPuBYFAoGBAMcP\nQ91mXQhcqSYGV7qF9HRzePm0PE9tN+v383hEtyy8xBJgPJ1J7OXWEnqD9u/ZIhP0\nMViVt+h7TOYjpcRoQL89KX9NptFk0hk0e9cyaMM8HzUGpJ8Ccnxn3lEAtK8TXt8u\nIIYJEFN2BJX36BbKc+rEwmq4um0kfwsViwbVtvJ7AoGBALiW6maJQVnLBNHoU+qZ\nJFYYgjQgWXeFggTwXaFzGr/lfZjrGzc2vIhKEocliXNgL2r8q5Qh7H0EGjViJXKR\nMtjfbkIsv4JbkvfED+Xs7EmqwdDpUZm482tHYGqpLjy7lNRrJkEcX/9pn9D+Jf/H\ngUCCLx5/AZju6nSunmrSsB+n\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-o2pvr@scankart-40ac1.iam.gserviceaccount.com",
  "client_id": "115609852691823809025",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-o2pvr%40scankart-40ac1.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


db = firestore.Client.from_service_account_info(service_account_info)

