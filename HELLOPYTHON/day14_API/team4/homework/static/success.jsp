<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	
	<%  
		
	 String irum = request.getParameter("pg_token");
		System.out.println(irum);
	%>
	
	
   <h1>결제 승인 페이지</h1>
   <form method="post" action="http://127.0.0.1:9998/approve">
      <button class="btn btn-warning">결제 완료/button>
    </form>
   
</body>
</html>