<?php
namespace sample\encryption;

class Certificate
{
    // Sample class for to generate and manage OpenSSL private/public keypairs.
    private object $privateKeyResource;
    private array $privateKeyDetails;

    public function __construct(
        private int $keyBits = 2048,
        private int $keyType = OPENSSL_KEYTYPE_RSA,
        private string $keyName = '',
        private string $keyPassword = '',
        private string $privateKey = '',
        private string $publicKey = ''
    ) {

    }

    public function generate(): bool
    {
        if (!$this->keyName) {
            printf("Key name was not set\n");
            return false;
        } else {
            $this->privateKeyResource = openssl_pkey_new([
                "private_key_bits" => $this->keyBits,
                "private_key_type" => $this->keyType
            ]);

            $this->privateKeyDetails = openssl_pkey_get_details($this->privateKeyResource);

//            print_r($privateKeyResource);
//            print_r($privateKeyDetails);
            return true;
        }
    }

    public function export(): bool
    {
        if (!$this->keyPassword) {
            printf("Key password was not set\n");
            return false;
        } else {
            $this->privateKey = dirname(__FILE__) . "/" . $this->keyName . "-private.pem";
            $this->publicKey = dirname(__FILE__) . "/" . $this->keyName . "-public.pem";
            printf("Exporting private key : %s\n", $this->privateKey);
            printf("Exporting public key  : %s\n", $this->publicKey);

//            print_r($this->privateKeyResource);
//            print_r($this->privateKeyDetails);
            openssl_pkey_export_to_file($this->privateKeyResource, $this->privateKey, $this->keyPassword);
            file_put_contents($this->publicKey, $this->privateKeyDetails["key"]);
            return true;
        }
    }

    public function __set(string $name, mixed $value): void
    {
        $this->{$name} = $value;
    }

    public function __get($name)
    {
        return $this->{$name};
    }
}
?>
