

function display(object, showButton, hideButton){
    $("#"+object).show();
    $("#"+showButton).hide();
    $("#"+hideButton).show();
}
function hide(object, showButton, hideButton){
    $("#"+object).hide();
    $("#"+showButton).show();
    $("#"+hideButton).hide();
}

$(document).ready(function(){
    $(".dropdown ul").each(function(i){
        $(this).attr("id", "dropdown"+ i)
    });
    var dropdown = $(".dropdown");
    dropdown.mouseenter(function(){
        var index = $(".dropdown").index(this);
        var menu="dropdown"+index;
        $("#"+menu).slideDown();
    });
    dropdown.mouseleave(function(){
        var index = $(".dropdown").index(this);
        var menu="dropdown"+index;
        $("#"+menu).slideUp();
    });
    $("#delete_project").click(function(){
        return confirm("Are you sure you wish to delete this project?");
    })
});
