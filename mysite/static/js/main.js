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

   
})

