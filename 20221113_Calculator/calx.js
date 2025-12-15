//電卓操作する際、まず下記基本の４個の機能を実装する
 
function update(_v) //1. HTMLのinputタグを更新する関数
{
   document.querySelector( 'input' ).value = _v
}

function num_click(_v) // 2.ボタン押されると、押されたボタンの値や記号が追加される
{
    document.querySelector( 'input' ).value += _v
}

function calc() //3.「=」ボタンが押されると、計算する
{
    const v = document.querySelector( 'input' ).value
    
    try{
        const f = new Function( 'return ' + v)
        update( f().toString() ) 
    } catch(error) {
        update(V = "計算不可") //4. 数字＋記号或いは記号が先に押された場合は、計算不可が表示される
    }
}


//操作していく上、０（ゼロ）が数字の前につかない・記号押しても連続にならない変数・関数等。

//変数・データ
var result = "";
// =で計算したかどうか
var is_calc = false;

//初期表示
window.onload = function () {
    result = document.getElementById('result');
  };

//初期画面とCLRボタン押した後に、０（ゼロ）以外の数字押されても、０（ゼロ）が頭につかないように
// 数字キー押下
function num_click(val){
    if(is_calc)  result.value = "0";
    is_calc = false;  
  
    if(result.value =="0" && val == "0"){
      result.value = "0";
    }else if(result.value == "0"){
      result.value = val;
    }else{
      result.value += val;
    }
  }

//連続入力にならないように：⓵＋⓶
//⓵演算子キーの機能
function ope_click(val){
  if(is_calc)  is_calc = false;
  
  if(is_ope_last()){
    result.value = result.value.slice(0, -1) + val;
  } else {
    result.value += val;
  }
}

//⓶入力されている値が演算子かどうかの確認と
function is_ope_last(){
    return ["+","-","x","/"].includes(result.value.toString().slice(-1));
  }