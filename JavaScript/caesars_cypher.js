function rot13(str) {
    var decoded = '';
    var string = str.split('');
    for (var letter in string){
      var asciiNum = string[letter].charCodeAt();
      if (asciiNum >= 65 && asciiNum <= 77){
        decoded += String.fromCharCode(asciiNum + 13);
      }
      else if ( asciiNum >= 78 && asciiNum <= 90){
        decoded += String.fromCharCode(asciiNum - 13);
      }
      else {
        decoded += string[letter];
      }
      }
      
    return decoded;
}

rot13("SERR PBQR PNZC.");