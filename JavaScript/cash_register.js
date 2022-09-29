function checkCashRegister(price, cash, cid) {
    var currencyUnit = {
      'ONE HUNDRED' : 100,
      'TWENTY'	: 20,
      'TEN' : 10,
      'FIVE' : 5,
      'ONE' : 1,
      'QUARTER' : 0.25,
      'DIME' : 0.10,
      'NICKEL' : 0.05,
      'PENNY' : 0.01,
    }
    
    let change = cash - price;
    let newChange = change;
    let status = ''
    var changeOutput = [];
    var total = 0;
    for (let i = 0; i < cid.length ; i++){
      total += cid[i][1]
    }
  
    let reverseCid = cid.reverse()
    
    for (const [key, value] of reverseCid) {
  
     let amount = 0; 
     while (newChange.toFixed(2) >= currencyUnit[key] && value > 0){
       amount += currencyUnit[key];
       newChange -= currencyUnit[key];
       value -= currencyUnit[key]; 
     }
     if (amount !== 0){
       changeOutput.push([key, amount]);
     }  
  
  }
  
  if (newChange > 0 ){
    status = 'INSUFFICIENT_FUNDS';
    changeOutput = [] 
  }
  else if (total == change){
    status = 'CLOSED';
    changeOutput = cid.reverse();
  }
  else {
    status = 'OPEN';
  }
  return {'status': status, 'change':changeOutput };
}
  
checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);