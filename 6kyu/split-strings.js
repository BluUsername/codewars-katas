function solution(str) {
  return (str + (str.length % 2 ? '_' : '')).match(/.{2}/g) || [];
}