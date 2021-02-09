package me.nassim.androidApp

import android.annotation.SuppressLint
import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText
import me.nassim.shared.Greeting
import androidx.recyclerview.widget.RecyclerView
import org.json.JSONArray
import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL

fun greet(): String {
    return Greeting().greeting()
}

class MainActivity : AppCompatActivity() {
    val list_room = ArrayList<Room>()
    val list = ArrayList<Range>()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val url = "https://mysafeinfo.com/api/data?list=presidents&format=json"
        val url2 = "http://10.0.2.2:8000/products/"

        AsyncTaskHandleJson().execute(url2)
    }

    @SuppressLint("StaticFieldLeak")
    inner class AsyncTaskHandleJson : AsyncTask<String, String, String>() {
        override fun doInBackground(vararg url: String?): String {
            val text: String
            val connection = URL(url[0]).openConnection() as HttpURLConnection
            try {
                connection.connect()
                text = connection.inputStream.use { it.reader().use{reader -> reader.readText()}}
            }finally {
                connection.disconnect()
            }
            return text
        }

        override fun onPostExecute(result: String?) {
            super.onPostExecute(result)
            handleJson(result)
        }
    }

    private fun handleJson(jsonString: String?) {

        val jsonObj = JSONObject(jsonString)
        val jsonArray = jsonObj.getJSONArray("products")



        for(i in 0 until jsonArray.length() ){
            val jsonObject = jsonArray.getJSONObject(i)

            list.add(
                Range(
                    jsonObject.getString("nom"),
                    jsonObject.getJSONArray("modules")
                )
            )
            println(list.last().module[0] is JSONArray)
        }

        /*val rangeRecyclerView = this.findViewById<RecyclerView>(R.id.module_recyclerview)
        val adapter = RangeAdapter(this,list)
        rangeRecyclerView.adapter = adapter*/
    }

    fun addRoom(view: View) {
        val roomName = this.findViewById<EditText>(R.id.et_room_name)
        list_room.add(
            Room(
                list_room.count()+1,
                roomName.text.toString(),
                null
            )
        )
        val roomRecyclerView = this.findViewById<RecyclerView>(R.id.room_recycler_view)
        val adapter = RoomAdapt(this,list_room,list)
        roomRecyclerView.adapter = adapter
    }
}
