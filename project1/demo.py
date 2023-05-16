import pandas as pd

df=pd.read_csv('Stock_ABAD1.csv')
df=df.drop(['<VALUE>','<VOL>','<TICKER>'],axis=1)
df1=df

print(df.columns)

#==========================SMA

SMA=[]

print(len(df['<CLOSE>']))

for i in range(len(df['<CLOSE>'])):
    if i<10:
        SMA.append(df['<CLOSE>'][i])
    else:
        
        sum=0
        j=10
        while j>0:
            
            sum+=df['<CLOSE>'][i-j]
            j-=1   
        avg=sum/10
        SMA.append(avg)    


print(len(SMA))

df['SMA']=SMA

#==========================SMA binary

SMA_b=[]

for i in range(len(df['<CLOSE>'])):
    if i<20:
        SMA_b.append(1)
    else:
        sma=df['SMA'][i]
        sum=0
        j=10
        while j>0:
            
            sum+=df['SMA'][i-j]
            j-=1   
        avg=sum/10
        if sma<avg:
            sma_b=0
        else:
            sma_b=1    
        SMA_b.append(sma_b)    


print(len(SMA_b))

df['SMA_b']=SMA_b


#==========================WMA

WMA=[]

for i in range(len(df['<CLOSE>'])):
    if i<10:
        WMA.append(df['<CLOSE>'][i])
    else:
        
        sum=0
        j=10
        while j>0:
            # print(j)
            sum+=j*(df['<CLOSE>'][i-j])
            j-=1 

        avg=sum/(10+9+8+7+6+5+4+3+2+1)
        WMA.append(avg)    


print(len(WMA))

df['WMA']=WMA

#==========================WMA binary

WMA_b=[]

for i in range(len(df['<CLOSE>'])):
    if i<20:
        WMA_b.append(1)
    else:
        wma=df['WMA'][i]
        sum=0
        j=10
        while j>0:
            
            sum+=df['WMA'][i-j]
            j-=1   
        avg=sum/10
        if wma<avg:
            wma_b=0
        else:
            wma_b=1    
        WMA_b.append(wma_b)    


print(len(WMA_b))

df['WMA_b']=WMA_b

#==========================MOM

MOM=[]



for i in range(len(df['<CLOSE>'])):
    if i<11:
        MOM.append(df['<CLOSE>'][i])
    else:
        j=11
        mom=df['<CLOSE>'][i]-df['<CLOSE>'][i-j]
        MOM.append(mom)    


print(len(MOM))

df['MOM']=MOM

#==========================MOM binary

MOM_b=[]



for i in range(len(df['<CLOSE>'])):
    if i<11:
        MOM_b.append(1)
    else:
       
        mom=df['MOM'][i]
        if mom>0:
            mom_b=1
        else:
            mom_b=0
        MOM_b.append(mom_b)    


print(len(MOM_b))

df['MOM_b']=MOM_b

#==========================STCK

STCK=[]

for i in range(len(df['<CLOSE>'])):
    if i<11:
        STCK.append(df['<CLOSE>'][i])
    else:
        close=df['<CLOSE>'][i]
        
        Ls=[]
        j=10
        while j>0:
            # print(j)
            Ls.append(df['<LOW>'][i-j])
            j-=1 
        LL=min(Ls)  

        Hs=[]
        j=10
        while j>0:
            # print(j)
            Hs.append(df['<HIGH>'][i-j])
            j-=1 
        HH=max(Ls)    

        stck=((close-LL)/(HH-LL))*100
    
        STCK.append(stck)    


print(len(STCK))

df['STCK']=STCK

#==========================STCK binary

STCK_b=[]



for i in range(len(df['<CLOSE>'])):
    if i<11:
        STCK_b.append(1)
    else:
       
        st1=df['STCK'][i-1]
        st2=df['STCK'][i]


        if st1<st2:
            stck_b=1
        else:
            stck_b=0  
        STCK_b.append(stck_b)    


print(len(STCK_b))

df['STCK_b']=STCK_b


#==========================LWR

LWR=[]

for i in range(len(df['<CLOSE>'])):
    if i<11:
        LWR.append(df['<CLOSE>'][i])
    else:
        close=df['<CLOSE>'][i]
        
        Ls=[]
        j=10
        while j>0:
            # print(j)
            Ls.append(df['<LOW>'][i-j])
            j-=1 
        LL=min(Ls)  

        Hs=[]
        j=10
        while j>0:
            # print(j)
            Hs.append(df['<HIGH>'][i-j])
            j-=1 
        HH=max(Ls)    

        lwr=((HH-close)/(HH-LL))*100
    
        LWR.append(lwr)    


print(len(LWR))

df['LWR']=LWR

#==========================LWR binary

LWR_b=[]



for i in range(len(df['<CLOSE>'])):
    if i<11:
        LWR_b.append(1)
    else:
       
        l1=df['LWR'][i-1]
        l2=df['LWR'][i]


        if l1<l2:
            lwr_b=1
        else:
            lwr_b=0  
        LWR_b.append(lwr_b)    


print(len(LWR_b))

df['LWR_b']=LWR_b

#==========================ADO

ADO=[]

for i in range(len(df['<CLOSE>'])):
    if i<11:
        ADO.append(df['<CLOSE>'][i])
    else:
        close=df['<CLOSE>'][i]
        LL=df['<LOW>'][i]  
        HH=df['<HIGH>'][i]    
        try:
            ado=((HH-close)/(HH-LL))*100
        except:
            ado=0    
    
        ADO.append(ado)    


print(len(ADO))

df['ADO']=ADO


#==========================ADO binary

ADO_b=[]



for i in range(len(df['<CLOSE>'])):
    if i<11:
        ADO_b.append(1)
    else:
       
        ad1=df['ADO'][i-1]
        ad2=df['ADO'][i]


        if ad1<ad2:
            ad_b=1
        else:
            ad_b=0  
        ADO_b.append(ad_b)    


print(len(ADO_b),'ado_b')

df['ADO_b']=ADO_b
#==========================CCI

CCI=[]

for i in range(len(df['<CLOSE>'])):
    if i<11:
        CCI.append(df['<CLOSE>'][i])
    else:
        close=df['<CLOSE>'][i]
        L=df['<LOW>'][i]  
        H=df['<HIGH>'][i]    

        M=(close+L+H)/3

        ms=0
        j=10
        while j>0:
            close1=df['<CLOSE>'][i-j]
            L1=df['<LOW>'][i-j]  
            H1=df['<HIGH>'][i-j]    

            m1=(close1+L1+H1)/3
            ms+=m1
            j-=1 
        SM=ms/10

        d=0
        j=10
        while j>0:
            close1=df['<CLOSE>'][i-j]
            L1=df['<LOW>'][i-j]  
            H1=df['<HIGH>'][i-j]    

            m1=(close1+L1+H1)/3
            d+=abs(m1-SM)
            j-=1 
        D=d/10

        cci=(M-SM)/(0.015*D)

        CCI.append(cci)    


print(len(CCI),'cci')

df['CCI']=CCI

#==========================CCI binary

CCI_b=[]



for i in range(len(df['<CLOSE>'])):
    if i<11:
        CCI_b.append(1)
    else:
       
       
        cci=df['CCI'][i]
        cc1=df['CCI'][i-1]


        if cci>200:
            cc_b=0
        elif cci<-200:
            cc_b=1  
        else:
            if cci>cc1:
                cc_b=1
            else:
                cc_b=0 


        CCI_b.append(cc_b)    



print(len(CCI_b),'cci_b')
df1['CCI_b']=CCI_b

#=======================Trend

trend=[]

for i in range(len(df['<CLOSE>'])):
    # print(i)
    if i<11:
        trend.append(1)
    else:
        c1=df['<CLOSE>'][i]
        if i!=len(df['<CLOSE>'])-1:
            c2=df['<CLOSE>'][i+1]
        else:
            c2=df['<CLOSE>'][i]
        if c2>=c1:
            tr=1
        else:
            tr=0           
    
        trend.append(tr)    


print(len(trend),'trend')
print('done')

df['TREND']=trend

df.to_csv('demopre.csv',index=False)