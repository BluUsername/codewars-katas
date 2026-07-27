function narcissistic(value) {
  const digits = String(value)
  const digitArray = digits.split("")
  const power = digitArray.length
  const sum = digitArray.reduce((total, digit) => {
    return total + Math.pow(Number(digit), power)
  }, 0)
  return sum === value
}
