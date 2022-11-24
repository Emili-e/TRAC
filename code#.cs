using System.Collections ;
using System.Collections.Generic ;
using UnityEngine ;

int a = 9 ;
int b ;
public class SetCursor : MonoBehaviour {
    public Texture2D eyecrossair ;
    public Texture2D basecursor ;
    public Texture2D directionright ;
    public Texture2D directionup ;
    public Texture2D directionleft ;
    public Texture2D directiondown ;

    public static float cursorState ;

    private void Awake() {
        DontDestroyOnLoad(this.gameObject) ;
    }

    // Use this for initialization
    void Start() {
    }

    // Update is called once per frame
    void Update() {
        if (cursorState == 1) {
            Vector2 cursorOffset1 = new Vector2(eyecrossair.width/2, eyecrossair.height) ;
            Cursor.SetCursor(eyecrossair, cursorOffset1, CursorMode.Auto) ;
        }

        if (cursorState == 0) {
            Vector2 cursorOffset0 = new Vector2(basecursor.width/2, basecursor.height) ;
            Cursor.SetCursor(basecursor, cursorOffset0, CursorMode.Auto) ;
        }

        if (cursorState == 2) {
            Vector2 cursorOffset2 = new Vector2(directionright.width/2, directionright.height) ;
            Cursor.SetCursor(directionright, cursorOffset2, CursorMode.Auto) ;
        }

        if (cursorState == 3) {
            Vector2 cursorOffset3 = new Vector2(directionup.width/2, directionup.height) ;
            Cursor.SetCursor(directionup, cursorOffset3, CursorMode.Auto) ;
        }

        if (cursorState == 4) {
            Vector2 cursorOffset4 = new Vector2(directionleft.width/2, directionleft.height) ;
            Cursor.SetCursor(directionleft, cursorOffset4, CursorMode.Auto) ;
        }

        if (cursorState == 5) {
            Vector2 cursorOffset5 = new Vector2(directiondown.width/2, directiondown.height) ;
            Cursor.SetCursor(directiondown, cursorOffset5, CursorMode.Auto) ;
        }
    }
} // test uwu