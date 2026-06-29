function toCamelCase(str) {
  return str
    .split(/[-_]/)
    .map((word, i) => i === 0 ? word : word.charAt(0).toUpperCase() + word.slice(1))
    .join('');
}
