#include<bits/stdc++.h>
using namespace std;
 main(){
    ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    string s;
    int currpage=1;

    while(getline(cin,s)){
        bool possibility = false;
        int i=0;
        while(i<s.length()&& s[i]==' ')i++;
        string num;
        while(i>1 && i<s.length() && s[i]>='0' && s[i] <='9'){
            num.push_back(s[i]);
            if(stoi(num)==currpage){
                possibility=true;
                cerr<<currpage<<"\n";
                currpage++;
                i++;
                break;
            }
            i++;
        }
        if(possibility){
            for(int j=i;j<s.length();j++){
                if(s[j]==-99 || s[j]==-100)cout<<'"';
                else if(s[j]==-90)cout<<"...";
                else if(s[j]==-104 || s[j]==-103)cout<<"'";
                else if(s[j]==-109 || s[j]==-108)cout<<"-";
                else if(s[j]>=0) cout<<s[j];
                }
            cout<<"\n";
        }
        else {
            for(auto ele : s){
                if(ele==-99 || ele==-100)cout<<'"';
                else if(ele==-90)cout<<"...";
                else if(ele==-104 || ele==-103)cout<<"'";
                else if(ele==-109 || ele==-108)cout<<"-";
                else if(ele>=0)cout<<ele;
            }
            cout<<"\n";
        }
    }


}