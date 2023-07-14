<?php
// Test script to generate OpenSSL certificate and encrypt data using said key.

require_once dirname(__FILE__) . "/certificate.php";
require_once dirname(__FILE__) . "/encrypt.php";

use sample\encryption\Certificate;
use sample\encryption\Encrypt;
use sample\encryption\Type;

$certificate = new Certificate();
//2048, OPENSSL_KEYTYPE_RSA);
$certificate->keyBits = 2048;
$certificate->keyType = OPENSSL_KEYTYPE_RSA;
$certificate->keyName = "Testing";
$certificate->keyPassword = "Testing123";

print("Key Bits    : " . $certificate->keyBits . "\n");
print("Key Type    : " . $certificate->keyType . "\n");
print("Key Name    : " . $certificate->keyName . "\n");
print("Key Password: " . $certificate->keyPassword . "\n");

$privateKey = $certificate->generate();
if ($privateKey) {
    $certificate->export();
}

printf("\n\nEncrypting: %s\n", $certificate->privateKey);

$encrypt = new Encrypt();
$file_encrypt = $encrypt->encrypt(file_get_contents($certificate->privateKey), Type::PUBLIC, $certificate->publicKey, false);
printf("\nEncrypted Data -\n");
printf("%s\n\n", $file_encrypt);
$file_decrypt = $encrypt->decrypt($file_encrypt, Type::PRIVATE, $certificate->privateKey, $certificate->keyPassword);
printf("Unencrypted data -\n");
printf("%s\n", $file_decrypt);
?>
