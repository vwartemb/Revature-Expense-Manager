error id: file://<WORKSPACE>/manager-app/src/main/java/com/revature/models/User.java
file://<WORKSPACE>/manager-app/src/main/java/com/revature/models/User.java
### com.thoughtworks.qdox.parser.ParseException: syntax error @[3,1]

error in qdox parser
file content:
```java
offset: 31
uri: file://<WORKSPACE>/manager-app/src/main/java/com/revature/models/User.java
text:
```scala
package com.revature.models;

c@@lapackage com.revature.models;

public class User {
    private int  id;
    private String username;
    private String password;
    private String role;

    // when you want to create an object first and set fields later.
    // so... User user = new User();
    public User() {}

    // Used when reading from the database
    // so... User user = new User(1, "john", "hashedpw", "employee");
    public User(int id, String username, String password, String role) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.role = role;
    }

    //Used when you want to create a new user (id is auto-generated)
    // so... User user = new User("john", "hashedpw", "employee");
    public User(String username, String password, String role) {
        this.username = username;
        this.password = password;
        this.role = role;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getRole() {
        return role;
    }
    public void setRole(String role) {
        this.role = role;
    }

    @java.lang.Override
    public java.lang.String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", role='" + role + '\'' +
                '}';
    }
}


```

```



#### Error stacktrace:

```
com.thoughtworks.qdox.parser.impl.Parser.yyerror(Parser.java:2025)
	com.thoughtworks.qdox.parser.impl.Parser.yyparse(Parser.java:2147)
	com.thoughtworks.qdox.parser.impl.Parser.parse(Parser.java:2006)
	com.thoughtworks.qdox.library.SourceLibrary.parse(SourceLibrary.java:232)
	com.thoughtworks.qdox.library.SourceLibrary.parse(SourceLibrary.java:190)
	com.thoughtworks.qdox.library.SourceLibrary.addSource(SourceLibrary.java:94)
	com.thoughtworks.qdox.library.SourceLibrary.addSource(SourceLibrary.java:89)
	com.thoughtworks.qdox.library.SortedClassLibraryBuilder.addSource(SortedClassLibraryBuilder.java:162)
	com.thoughtworks.qdox.JavaProjectBuilder.addSource(JavaProjectBuilder.java:174)
	scala.meta.internal.mtags.JavaMtags.indexRoot(JavaMtags.scala:49)
	scala.meta.internal.mtags.MtagsIndexer.index(MtagsIndexer.scala:22)
	scala.meta.internal.mtags.MtagsIndexer.index$(MtagsIndexer.scala:21)
	scala.meta.internal.mtags.JavaMtags.index(JavaMtags.scala:39)
	scala.meta.internal.mtags.Mtags.index(Mtags.scala:106)
	scala.meta.internal.mtags.Mtags.allSymbols(Mtags.scala:21)
	scala.meta.internal.mtags.SymbolIndexBucket.allSymbols(SymbolIndexBucket.scala:293)
	scala.meta.internal.mtags.SymbolIndexBucket.addMtagsSourceFile(SymbolIndexBucket.scala:304)
	scala.meta.internal.mtags.SymbolIndexBucket.$anonfun$query0$1(SymbolIndexBucket.scala:220)
	scala.meta.internal.mtags.SymbolIndexBucket.$anonfun$query0$1$adapted(SymbolIndexBucket.scala:220)
	scala.collection.immutable.Set$Set1.foreach(Set.scala:177)
	scala.meta.internal.mtags.SymbolIndexBucket.query0(SymbolIndexBucket.scala:220)
	scala.meta.internal.mtags.SymbolIndexBucket.query(SymbolIndexBucket.scala:193)
	scala.meta.internal.mtags.OnDemandSymbolIndex.$anonfun$findSymbolDefinition$1(OnDemandSymbolIndex.scala:143)
	scala.collection.immutable.List.flatMap(List.scala:283)
	scala.meta.internal.mtags.OnDemandSymbolIndex.findSymbolDefinition(OnDemandSymbolIndex.scala:143)
	scala.meta.internal.mtags.OnDemandSymbolIndex.definition(OnDemandSymbolIndex.scala:48)
	scala.meta.internal.metals.Docstrings.indexSymbol(Docstrings.scala:138)
	scala.meta.internal.metals.Docstrings.documentation(Docstrings.scala:49)
	scala.meta.internal.metals.MetalsSymbolSearch.documentation(MetalsSymbolSearch.scala:47)
	scala.meta.internal.pc.JavaMetalsGlobal.documentation(JavaMetalsGlobal.scala:187)
	scala.meta.internal.pc.JavaHoverProvider.$anonfun$hoverOffset$1(JavaHoverProvider.scala:67)
	scala.Option.map(Option.scala:242)
	scala.meta.internal.pc.JavaHoverProvider.hoverOffset(JavaHoverProvider.scala:57)
	scala.meta.internal.pc.JavaHoverProvider.hover(JavaHoverProvider.scala:37)
	scala.meta.internal.pc.JavaPresentationCompiler.hover(JavaPresentationCompiler.scala:80)
	scala.meta.internal.metals.Compilers.$anonfun$hover$1(Compilers.scala:1134)
	scala.meta.internal.metals.Compilers.$anonfun$withPCAndAdjustLsp$12(Compilers.scala:1628)
	scala.Option.map(Option.scala:242)
	scala.meta.internal.metals.Compilers.$anonfun$withPCAndAdjustLsp$10(Compilers.scala:1628)
	scala.Option.flatMap(Option.scala:283)
	scala.meta.internal.metals.Compilers.withPCAndAdjustLsp(Compilers.scala:1610)
	scala.meta.internal.metals.Compilers.hover(Compilers.scala:1129)
	scala.meta.internal.metals.MetalsLspService.$anonfun$hover$1(MetalsLspService.scala:985)
	scala.meta.internal.metals.CancelTokens$.future(CancelTokens.scala:38)
	scala.meta.internal.metals.MetalsLspService.hover(MetalsLspService.scala:983)
	scala.meta.internal.metals.WorkspaceLspService.hover(WorkspaceLspService.scala:524)
	scala.meta.metals.lsp.DelegatingScalaService.hover(DelegatingScalaService.scala:78)
	java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:103)
	java.base/java.lang.reflect.Method.invoke(Method.java:580)
	org.eclipse.lsp4j.jsonrpc.services.GenericEndpoint.lambda$recursiveFindRpcMethods$0(GenericEndpoint.java:65)
	org.eclipse.lsp4j.jsonrpc.services.GenericEndpoint.request(GenericEndpoint.java:128)
	org.eclipse.lsp4j.jsonrpc.RemoteEndpoint.handleRequest(RemoteEndpoint.java:265)
	org.eclipse.lsp4j.jsonrpc.RemoteEndpoint.consume(RemoteEndpoint.java:195)
	org.eclipse.lsp4j.jsonrpc.json.StreamMessageProducer.handleMessage(StreamMessageProducer.java:189)
	org.eclipse.lsp4j.jsonrpc.json.StreamMessageProducer.listen(StreamMessageProducer.java:97)
	org.eclipse.lsp4j.jsonrpc.json.ConcurrentMessageProcessor.run(ConcurrentMessageProcessor.java:97)
	java.base/java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:572)
	java.base/java.util.concurrent.FutureTask.run(FutureTask.java:317)
	java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
	java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
	java.base/java.lang.Thread.run(Thread.java:1583)
```
#### Short summary: 

QDox parse error in file://<WORKSPACE>/manager-app/src/main/java/com/revature/models/User.java