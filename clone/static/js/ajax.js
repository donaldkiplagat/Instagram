$(document).ready(function () {
    $(".like").on("click", function (event) {
        let comid = $(this).attr("data-comid");
        $.get("/profile/like/", {"post_id": comid}, function (data, status) {
            $(this).hide();
        });
     });
});
