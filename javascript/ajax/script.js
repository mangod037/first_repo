// + 버튼 클릭 시, input fade 토글
$('#plus').on('click', function(){
    $('#input').fadeToggle()
})

// trash icon 클릭 시, 500ms 간 fadeOut 후 사라짐
$(document).on('click', '.list i',function(event){
    $(this).parent().parent().fadeOut(500)
    event.stopPropagation()
})

// 작성된 리스트 누르면 .complete라는 클래스 토글
$(document).on('click', '.list div',function(){
    $(this).toggleClass('complete')
})

// 입력 후 엔터 입력 시, 새로운 리스트 생성
$('#input').on('keypress', function(event){
    if (event.keyCode===13) {
        $('.list').append('<div>'+ '- '+ $('#input').val() +'<span><i class="far fa-trash-alt icon"></i></span></div>')
        $('#input').val('')
    }
})

// 상단의 trash 버튼 클릭 시, 완료된 리스트 모두 삭제
$('#delete_all').on('click', function(){
    $('.complete').fadeOut(500)
})