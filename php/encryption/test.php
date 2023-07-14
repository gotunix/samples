<?php
// Test script to generate OpenSSL certificate and encrypt data using said key.

require_once dirname(__FILE__) . "/certificate.php";

use sample\encryption\Certificate;

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
?>
