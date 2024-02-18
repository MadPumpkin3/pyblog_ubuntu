(function () {
    var cx = '파트너 아이디';
    var gcse = document.createElement('script');
    gcse.type = 'text/javascript';
    gcse.async = true;
    gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(gcse, s);    
  })();
  
  function googleCustomSearchExecute() {
      var input = document.getElementById('cse-search-input-box-id');
      var element = google.search.cse.element.getElement('searchresults-only0');
      console.log("googleCustomSearchExecute")
      console.log("element : ",element)
      if (input.value == '') {
        element.clearAllResults();
      } else {
        element.execute(input.value);
      }
      return false;
    }