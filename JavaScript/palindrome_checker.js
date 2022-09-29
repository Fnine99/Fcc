function palindrome(str) {
    const x = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    let len = x.length
    var first_half = x.substring(0, Math.floor(len/2))
    var second_half = x.substring(Math.round(len/2),len)
    return (first_half === second_half.split("").reverse().join(""))
}
  
  
console.log(palindrome('oyo'))