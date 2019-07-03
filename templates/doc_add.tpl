<form action=$SELF_URL METHOD=post name=FORM_NAS ID='FORM_NAS' class='form-horizontal' role='form'>
  <fieldset>

    <input type=hidden name='index' value='$index'>
    %ID%

    <div class='box box-theme box-big-form'>
      <div class='box-header with-border'><h4 class='box-title'>%TITLE%</h4></div>
      <div class='box-body'>

        <div class='form-group'>
          <label for='NAS_IP' class='control-label col-md-4 required'>WIKI URL:</label>

          <div class='col-sm-8'>
            <input type=text class='form-control ip-input' required id='NAS_IP' name='WIKI' value='%WIKI%'>
          </div>
        </div>
        <div class='form-group'>
          <label for='NAS_NAME' class='control-label col-md-4 required'>CONFLUENCE URL:</label>

          <div class='col-md-8'>
            <input type='text' class='form-control' id='CONFLUENCE' name='CONFLUENCE' value='%CONFLUENCE%' required >
          </div>
        </div>

        <div class='box-footer'>
         %SUBMIT%
        </div>
      </div>

    </div>

  </fieldset>
</form>
