public class Location{
    private int matchIndex;
    private boolean match;

    public Location(){
        matchIndex = -1;
        match = false;
    }
    public void setMatchIndex(int index){
        matchIndex = index;
    }
    public void setMatch(boolean match){
        this.match = match;
    }
    public int getMatchIndex(){
        return matchIndex;
    }
    public boolean getMatch(){
        return match;
    }
}