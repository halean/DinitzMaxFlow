class Graph(object):
    
    def add(self,u,v,c):
        self.to.append(v)
        self.cap.append(c)
        self.flow.append(0)
        self.next(append(fin[u]))
        self.fin[u]=self.nEdge
        self.nEdge=self.nEdge+1

        self.to.append(u)
        self.cap.append(c)
        self.flow.append(0)
        self.next(append(fin[v]))
        self.fin[v]=self.nEdge
        self.nEdge=self.nEdge+1

    def __init__(self,source,sink,n):
        self.nEdge=0
        self.to=[]
        self.cap=[]
        self.flow=[]
        self.source=source
        self.sink=sink
        self.nNode=n
        self.fin=[-1 for i in range(0,self.nNode+1)]
        self.Q=[-2 for i in range(0,self.nNode+1)]
        self.pro=[0 for i in range(0,self.nNode+1)]
    def bfs(self):
        self.dist=[-1 for i in range (0,self.nNode)]
        st=0
        en=0
        self.dist[self.source]=0
        Q[en]=self.source
        en+=1
        while(st<en):
            u=Q[st]
            st+=1
            i=fin[u]
            while(i>=0):
                v=to[i]
                if(self.flow[i]<self.cap[i] and self.dist[v]==-1):
                    dist[v]=dist[u]+1
                    Q[en]=v
                    en+=1
                i=self.next[i]
        return self.dist[self.sink]!=-1

    def dfs(self,u,fl):
        if(u==self.sink):
            return fl
        e=self.pro[u]
        while(e>=0):
            v=to[e]
            if(self.flow[e]<cap[e] and self.dist[v]==self.dist[u]+1):
                df=dfs(v,min(self.cap[e],self.flow[e],fl))
                if(df>0):
                    self.flow[e]+=df
                    self.flow[e^1]-=df
                    return df
            self.pro[u]=self.next[pro[u]]
            e=self.pro[u]
        return 0

    def dinitz(self):
        ret=0
        df=0
        while(self.bfs()):
            for i in range(1,nNode+1):
                self.pro[i]=self.fin[i]
            while(true):
                df=self.dfs(source,10000000)
                if(df>0):
                    ret+=df
                else:
                    break
        return ret












