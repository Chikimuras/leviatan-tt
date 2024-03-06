<?php

/**
 * Check if a string is a palindrome
 * @param string $string
 * @return bool
 */
function isPalindrome($string): bool
{
    $cleanString = strtolower(preg_replace('/[^A-Za-z0-9]/', '', $string));
    $reverseString = strtr($cleanString, 'àáâäãåçèéêëìíîïñòóôöõùúûüýÿ', 'aaaaaaceeeeiiiinooooouuuuyy');

    for ($i = 0; $i < strlen($reverseString) / 2; $i++) {
        if ($reverseString[$i] !== $reverseString[strlen($reverseString) - $i - 1]) {
            return false;
        }
    }

    return true;
}
$user_input = readline('Tapez un mot: ');

echo isPalindrome($user_input) ? 'True' : 'False';