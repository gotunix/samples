<?php
namespace sample\encryption;

enum Type {
    case PUBLIC;
    case PRIVATE;
}

class Encrypt
{
    // Test Encryption class (used to encrypt strings using public/private keypairs and OpenSSL
    public function encrypt($source, $type, $key, $keyPassword): mixed
    {
        if ($type === Type::PUBLIC) {
            printf("Loading public_key: %s\n", $key);
            $publicKey = file_get_contents($key);
            $publicKey = openssl_get_publickey($publicKey);
            if (!$publicKey) {
                printf("Error loading public_key: %s\n", $Key);
                var_dump(openssl_error_string());
                return false;
            } else {
                $data = str_split($source, 214);
                $result = "";
                foreach ($data as $d) {
                    if (openssl_public_encrypt($d, $encrypted, $publicKey, OPENSSL_PKCS1_OAEP_PADDING)) {
                        $result .= $encrypted;
                    }
                }
                return base64_encode($result);
            }
        }
    }


    public function decrypt($source, $type, $key, $keyPassword): mixed
    {
        if ($type === Type::PRIVATE) {
            printf("Loading private key: %s\n", $key);
            if (!$keyPassword) {
                printf("No password supplied\n");
                return false;
            } else {
                $privateKey = file_get_contents($key);
                $privateKeyResource = openssl_pkey_get_private($privateKey, $keyPassword);
                if (!$privateKeyResource) {
                    printf("Error loading private key\n");
                    var_dump(openssl_error_string());
                    return false;
                } else {
                    $data = str_split(base64_decode($source), 256);
                    $result = "";
                    foreach ($data as $d) {
                        if (openssl_private_decrypt($d, $decrypted, $privateKeyResource, OPENSSL_PKCS1_OAEP_PADDING)) {
                            $result .= $decrypted;
                        }
                    }
                }
                return $result;
            }
        }
    }
}
