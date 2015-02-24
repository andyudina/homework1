#! /usr/bin/python

from cgi import parse_qs, escape

html = '''
<html>
   <body>
       <p><h1>%s<h1></p><br>
       <ul>Get parameters:
       %s
       </ul>
       <ul>Post parameters: 
       %s
       </ul>
   </body>
</html>
'''
def application (environ, start_response):
    status = '200 OK'
    output = 'Hello world!  '
   
    # GET PARAMS:
    qs = parse_qs(environ['QUERY_STRING'])
    #get_params = ' '.join(['       <li>%s = %s</li>' % (key, escape(qs[key][0])) for key in qs])
    get_params = ''.join(['%s = %s, ' % (key, escape(qs[key][0])) for key in qs])
    # POST PARAMS:
    try:
        request_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_size = 0
    request_body = environ['wsgi.input'].read(request_size)
    qs = parse_qs(request_body)
    #post_params = ' '.join(['       <li>%s = %s</li>' % (key, escape(qs[key][0])) for key in qs])
    post_params = ' '.join(['%s = %s, ' % (key, escape(qs[key][0])) for key in qs])

    #RESPONSE:

    #response = html % (output, get_params or '<li>No Get Params</li>', post_params or '<li>No Post Params</li>' )
    response = output + 'GET: ' + get_params + 'POST: ' + post_params
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(response)))]

    start_response(status, response_headers)
    return [response]
