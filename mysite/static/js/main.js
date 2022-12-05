$('#btndescription').click(()=>{
    $('.productsection2').hide();
    $('.productsection1').show();
    $('#btndescription').addClass('btnactive');
    $('#btnspecialization').removeClass('btnactive');
    
});

$('#btnspecialization').click(()=>{
     $('.productsection1').hide();
    $('.productsection2').show();
    $('#btnspecialization').addClass('btnactive');
    $('#btndescription').removeClass('btnactive');

   
});


$('#productbtnminus').click(()=>{
   let prodquantity = $('#productquantity').val()
   prodquantity = parseInt(prodquantity) - 1
   if (prodquantity >= 0){
   $('#productquantity').val(prodquantity)
   }
   else{
   $('#productquantity').val('0');

   }

})

$('#productbtplus').click(()=>{
   let prodquantity = $('#productquantity').val()
   prodquantity = parseInt(prodquantity) + 1
   $('#productquantity').val(prodquantity)

})

$('#addtocartbtn').click(()=>{
$('#countabsoluteinput').val($('#productquantity').val())

})



//    console.log($('#productquantity').val()) ;
