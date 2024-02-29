$(document).ready(function() {
    $('#mail_pop_link').click(function(e) {
        e.preventDefault(); // 기본 동작 중단
        $('#mail_pop').modal('show'); // 모달 열기
    });
});


function fn_sendmail(){
    var wordForm = new FormData();
    wordForm.append('csrfmiddlewaretoken', document.mailForm.csrfmiddlewaretoken.value);
    wordForm.append('mailBody', $('#floatingTextarea').val().replace(/\n/g,"<br>"));

    $.ajax({
        type: "post",
        url: location.protocol + "//" + location.host + "/mailsend.do",
        contentType: false,
        processData: false,
        data: wordForm,
        dataType: "json",
        success: function(data){
            if(data.isSend.count == 1){
                alert("메일 발송이 완료되었습니다.");
                $('#floatingTextarea').val('');
                $('.close').click();
            }
            else{
                alert("실패하였습니다. 잠시후에 다시 시도해주세요.");
            }
        },
    });
}