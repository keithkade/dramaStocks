$(function() {
  $('i.search, i.exit').click(function() {
    $('section.search').fadeToggle(500);
    $('input.search').focus();
  });
})
