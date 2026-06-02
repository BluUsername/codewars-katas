// Kata: Does my number look big in this? (6kyu)
// https://www.codewars.com/kata/5287e858c6b5a9678200083c

function narcissistic(value) {
  const digits = String(value)
  const digitArray = digits.split("")
  const power = digitArray.length
  const sum = digitArray.reduce((total, digit) => {
    return total + Math.pow(Number(digit), power)
  }, 0)
  return sum === value
}
